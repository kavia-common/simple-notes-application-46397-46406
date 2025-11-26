from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from .models import Note
from .serializers import NoteSerializer


# PUBLIC_INTERFACE
@api_view(['GET'])
def health(request):
    """
    Health check endpoint to verify the server is running.

    Returns:
        200 OK with a simple JSON message.
    """
    return Response({"message": "Server is up!"})


class NoteViewSet(viewsets.ModelViewSet):
    """
    PUBLIC_INTERFACE
    A viewset providing standard CRUD actions for Note.

    list:
        Retrieve a list of notes.

    retrieve:
        Retrieve a single note by ID.

    create:
        Create a new note.

    update:
        Update an existing note (full update).

    partial_update:
        Partially update an existing note.

    destroy:
        Delete a note by ID.
    """
    queryset = Note.objects.all().order_by("-updated_at")
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="notes_list",
        operation_summary="List notes",
        operation_description="Retrieve a list of notes ordered by most recently updated.",
        responses={200: NoteSerializer(many=True)},
        tags=["notes"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_retrieve",
        operation_summary="Retrieve note",
        operation_description="Retrieve a single note by its ID.",
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_create",
        operation_summary="Create note",
        operation_description="Create a new note with title and optional content.",
        request_body=NoteSerializer,
        responses={201: NoteSerializer()},
        tags=["notes"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_update",
        operation_summary="Update note",
        operation_description="Update an existing note by ID (full update).",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_partial_update",
        operation_summary="Partially update note",
        operation_description="Partially update an existing note by ID.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()},
        tags=["notes"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="notes_destroy",
        operation_summary="Delete note",
        operation_description="Delete a note by ID.",
        responses={204: "No Content"},
        tags=["notes"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
