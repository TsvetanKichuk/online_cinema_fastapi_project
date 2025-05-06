import pytest
from datetime import date
from fastapi import UploadFile
from fastapi.exceptions import ValidationError
from src.database.models.accounts import GenderEnum
from src.schemas.profiles import ProfileRequestSchema


def test_profile_request_schema_valid_data():
    mock_file = UploadFile(filename="example.jpg")  # Mocked upload file
    valid_data = {
        "first_name": "John",
        "last_name": "Doe",
        "gender": GenderEnum.MALE,
        "date_of_birth": date(1990, 1, 1),
        "info": "Some info about John",
        "avatar": mock_file,
    }
    profile = ProfileRequestSchema(**valid_data)
    assert profile.first_name == "John"
    assert profile.last_name == "Doe"
    assert profile.gender == GenderEnum.MALE
    assert profile.date_of_birth == date(1990, 1, 1)
    assert profile.info == "Some info about John"
    assert profile.avatar == mock_file


def test_profile_request_schema_missing_required_field():
    mock_file = UploadFile(filename="example.jpg")
    invalid_data = {
        "first_name": "John",
        "last_name": "Doe",
        "gender": GenderEnum.MALE,
        "date_of_birth": date(1990, 1, 1),
    }  # Missing 'info' and 'avatar'

    with pytest.raises(ValidationError):
        ProfileRequestSchema(**invalid_data)


def test_profile_request_schema_invalid_date():
    mock_file = UploadFile(filename="example.jpg")
    invalid_data = {
        "first_name": "John",
        "last_name": "Doe",
        "gender": GenderEnum.MALE,
        "date_of_birth": "invalid-date",  # Invalid date format
        "info": "Some info about John",
        "avatar": mock_file,
    }

    with pytest.raises(ValidationError):
        ProfileRequestSchema(**invalid_data)


def test_as_form_method():
    mock_file = UploadFile(filename="example.jpg")
    profile = ProfileRequestSchema.as_form(
        first_name="Jane",
        last_name="Doe",
        gender=GenderEnum.FEMALE,
        date_of_birth=date(1995, 12, 25),
        info="Some info about Jane",
        avatar=mock_file,
    )
    assert profile.first_name == "Jane"
    assert profile.last_name == "Doe"
    assert profile.gender == GenderEnum.FEMALE
    assert profile.date_of_birth == date(1995, 12, 25)
    assert profile.info == "Some info about Jane"
    assert profile.avatar == mock_file
