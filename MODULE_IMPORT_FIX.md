# Module Import Fix

## Problem
The backend server was failing to start with the following error:
```
Error: Cannot find module '../models/SubjectProgressDetail'
```

## Root Cause
There was a mismatch between the model file name and the import statement:
- The model file was named `SubjectProgress.js`
- The import statement was trying to import `../models/SubjectProgressDetail`
- The model inside the file was correctly exported as `SubjectProgressDetail`

## Solution
Fixed the import statement in `emolearn/backend/services/realtimeService.js`:

### Before
```javascript
const SubjectProgressDetail = require('../models/SubjectProgressDetail');
```

### After
```javascript
const SubjectProgressDetail = require('../models/SubjectProgress');
```

## Verification
1. ✅ Import statement now correctly references the existing file
2. ✅ Model name matches the export in the SubjectProgress.js file
3. ✅ Node.js can successfully import the realtimeService.js module
4. ✅ No more MODULE_NOT_FOUND errors

## Files Modified
- `emolearn/backend/services/realtimeService.js` (line 6)

## Expected Result
The backend server should now start without the import error and properly handle subject progress details in real-time updates.