
## Endpoints

/api

GET, POST
/tracks
/bullets
/streaks

GET, POST
/tracks/<track_id>/entries
/bullets/<bullet_id>/entries
/streaks/<streak_id>/entries

PUT, DELETE
/tracks/<track_id>
/bullets/<bullet_id>
/streaks/<streak_id>

GET, POST, PUT, DELETE
/tracks/entries
/bullets/entries
/streaks/entries

GET, POST, PUT, DELETE
/tracks/entries/<int:id>
/bullets/entries/<int:id>
/streaks/entries/<int:id>


## Authentication

Header
- Authorization: Bearer <API-Key>
- X-API-KEY: <API-Key>