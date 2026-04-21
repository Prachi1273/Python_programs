# Real-Time Student Progress & Activity Tracking - Implementation Guide

## Overview
This document explains the real-time tracking system for student progress and recent activity in the EmoLearn platform.

## Components & Files Modified

### 1. **New Hook: `useActivityTracking.js`**
**Location:** `frontend/src/hooks/useActivityTracking.js`

**Purpose:** Custom React hook that manages activity tracking with batching to avoid excessive API calls.

**Features:**
- Queues activities and flushes them periodically (10 seconds for regular activities, 500ms for quiz/module completion)
- Automatically sends pending activities before unmount
- Prevents duplicate tracking for guest users
- Handles errors and re-queues failed activities

**Usage:**
```javascript
import useActivityTracking from '../../hooks/useActivityTracking';

// In your component
const { trackActivity, flush } = useActivityTracking();

// Track an activity
trackActivity({
  type: 'module_completed', // or 'quiz_completed', 'content_viewed'
  subject: 'mathematics',
  module: 0,
  score: 95, // Only for quiz_completed
  duration: 300, // in seconds
  emotionData: detectedEmotion // Optional emotion data
});

// Manually flush pending activities
await flush();
```

### 2. **Updated: `LearningPage.js`**
**Location:** `frontend/src/pages/LearningPage/LearningPage.js`

**Changes:**
- Imported `useActivityTracking` hook
- Added hook initialization in component
- Modified `handleNextModule()` to call `trackActivity()` instead of making direct API calls
- Activities are now batched and sent efficiently

**Key Function:**
```javascript
const handleNextModule = async () => {
  if (currentModule < 2) {
    // Track module completion
    if (user && user._id && !user.isGuest) {
      trackActivity({
        type: 'module_completed',
        subject: currentSubject,
        module: currentModule,
        duration: 300,
        emotionData: detectedEmotion
      });
    }
    
    setCurrentModule(prev => prev + 1);
    setProgress(0);
    setIsPlaying(false);
  }
};
```

### 3. **Enhanced: `DashboardPage.js`**
**Location:** `frontend/src/pages/DashboardPage/DashboardPage.js`

**Improvements:**
- Added **polling mechanism**: Dashboard refreshes progress data every 10 seconds
- Improved real-time updates via WebSocket listener
- Better extraction and display of recent activity
- Smooth updates without manual page refresh

**Polling Implementation:**
```javascript
// Fetch data immediately
fetchData();

// Set up polling to refresh every 10 seconds
const pollInterval = setInterval(() => {
  fetchData();
}, 10000);

// Clean up on unmount
return () => {
  clearInterval(pollInterval);
  // ... other cleanup
};
```

## Data Flow

### Activity Tracking Flow
```
LearningPage (module/quiz complete)
    ↓
trackActivity() from useActivityTracking
    ↓
Queue activity in memory (activityQueueRef)
    ↓
Timer: 500ms (for module/quiz) or 10s (for other activities)
    ↓
progressService.trackModuleCompletion() / trackQuizCompletion()
    ↓
Backend: POST /api/progress/:userId/update
    ↓
Backend updates Progress document + recent activity
    ↓
Broadcast via WebSocket or wait for polling
    ↓
DashboardPage receives update
    ↓
UI updates with new progress & activity
```

## Backend Integration

### Progress Update Endpoint
**Endpoint:** `POST /api/progress/:userId/update`

**Request Body:**
```javascript
{
  subject: 'mathematics',
  action: 'module_completed',  // or 'quiz_completed', 'content_viewed'
  score: 95,                   // Only for quiz
  moduleCompleted: true,       // Only for module completion
  timeSpent: 300               // In seconds
}
```

**What Gets Updated:**
1. **Recent Activity Array:** New activity entry added
2. **Subject Progress:** Modules completed, progress percentage, last accessed
3. **Overall Progress:** Recalculated based on all subjects
4. **Active Minutes:** Updated with time spent
5. **Subject Progress Details:** Detailed historical records created

## Real-Time Data Updates

### Polling Method (Default)
- Dashboard polls every **10 seconds**
- Fetches updated progress data and recent activity
- Provides consistent updates even without WebSocket
- Lower latency compared to manual refresh

### WebSocket Method (Optional)
- Real-time updates via `studentRealtimeService`
- Instant updates when data changes
- More efficient for frequent updates
- Requires WebSocket connection setup

### Emotion Tracking
- Emotions logged via `progressService.logEmotion()`
- Added to emotion history in Progress document
- Used for emotion trend analysis

## Frontend Services

### `progressService` Methods

#### `trackModuleCompletion(userId, subject, timeSpent, action)`
Tracks when a student completes a module.

#### `trackQuizCompletion(userId, subject, score, timeSpent)`
Tracks when a student completes a quiz with their score.

#### `trackContentView(userId, subject, timeSpent)`
Tracks when a student views learning content.

#### `getProgress(userId)`
Fetches complete progress data including recent activity and emotion history.

#### `logEmotion(userId, emotionData)`
Logs detected emotion to the database.

## Database Schema Updates

### Progress Model Fields
- `recentActivity`: Array of activity records
  - `subject`: Subject name
  - `action`: Action type (module_completed, quiz_completed, content_viewed)
  - `timestamp`: When activity occurred
  - `score`: Score if applicable
  - `type`: Activity type enum

- `emotionHistory`: Array of emotion detections
  - `emotion`: Detected emotion
  - `confidence`: Confidence level
  - `timestamp`: When detected

## Testing & Verification

### How to Test Real-Time Tracking

1. **Test Module Completion:**
   - Navigate to LearningPage
   - Start a module
   - Click "Next Module" button
   - Check DashboardPage → Recent Activity should show new entry within 10 seconds

2. **Test Quiz Completion:**
   - Complete a quiz modal
   - DashboardPage should show quiz completion in recent activity

3. **Verify WebSocket Updates:**
   - Open browser DevTools → Network → WS
   - Look for real-time service connection
   - Watch for PROGRESS_UPDATE messages

4. **Check Database:**
   ```javascript
   // In MongoDB
   db.progresses.findOne({ userId: ObjectId("...") })
   // Look at recentActivity and emotionHistory arrays
   ```

## Troubleshooting

### Activities Not Showing in Recent Activity

**Problem:** Module/quiz completed but not showing in Recent Activity

**Solutions:**
1. Check if user is a guest (guest activities aren't tracked)
2. Verify backend is receiving POST request to `/api/progress/:userId/update`
3. Check browser console for errors
4. Verify MongoDB connection and Progress record exists
5. Wait up to 10 seconds for polling to fetch latest data

### Delayed Activity Updates

**Problem:** Takes longer than 10 seconds to see updates

**Solutions:**
1. WebSocket may not be connected - check browser console
2. Backend may be slow - check server logs
3. Manually refresh the page to force immediate fetch
4. Check network tab in DevTools for failed requests

### Emotion Data Not Recording

**Problem:** Emotion data not saved to database

**Solutions:**
1. Verify emotion detection is working in LearningPage
2. Check if `progressService.logEmotion()` is being called
3. Verify backend emotion endpoint is accessible
4. Check browser DevTools console for errors

## Performance Considerations

1. **Polling Interval:** 10 seconds balances responsiveness with server load
2. **Activity Batching:** Reduces API calls by grouping activities
3. **Emotion History:** Capped at 50 entries per user for query performance
4. **Recent Activity:** Limited to 4 entries displayed on dashboard
5. **WebSocket:** Optional but recommended for high-frequency updates

## Future Enhancements

1. **WebSocket Optimization:** Implement room-based subscriptions
2. **Real-time Collaboration:** Show other students' progress
3. **Instant Notifications:** Alert students of achievements
4. **Activity Analytics:** Detailed activity breakdown by time, subject, type
5. **Smart Caching:** Implement IndexedDB for offline tracking

## Configuration

### Polling Interval (Frontend)
**File:** `DashboardPage.js`
**Line:** `const pollInterval = setInterval(() => { fetchData(); }, 10000);`
**Value:** 10000ms (10 seconds)
**To Change:** Update the interval value

### Activity Flush Timing (Hook)
**File:** `useActivityTracking.js`
**Module/Quiz Completion:** 500ms
**Other Activities:** 10000ms
**To Change:** Update timeout values in `trackActivity()` method

## Related Files
- Backend: `/api/progress/:userId/update`
- Backend: `/api/progress/:userId`
- Backend: `/api/emotions/detect`
- Database: `Progress` model
- Database: `SubjectProgress` model

---

**Last Updated:** November 11, 2025
**Version:** 1.0
