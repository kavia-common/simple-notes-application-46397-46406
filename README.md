# simple-notes-application-46397-46406

Notes Backend (Django + DRF)

Endpoints:
- Swagger UI: /docs
- Redoc: /redoc
- Health: /api/health/
- Notes CRUD: /api/notes/ and /api/notes/{id}/

Sample cURL:

# Health
curl -s https://<host>:3001/api/health/

# Create a note
curl -s -X POST https://<host>:3001/api/notes/ \
  -H "Content-Type: application/json" \
  -d '{"title":"First Note","content":"Hello world"}'

# List notes
curl -s https://<host>:3001/api/notes/

# Retrieve a note
curl -s https://<host>:3001/api/notes/1/

# Update a note
curl -s -X PUT https://<host>:3001/api/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated","content":"Changed"}'

# Partial update
curl -s -X PATCH https://<host>:3001/api/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"content":"Patched"}'

# Delete
curl -s -X DELETE https://<host>:3001/api/notes/1/
