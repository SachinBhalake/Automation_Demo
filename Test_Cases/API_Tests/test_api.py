import pytest
from Utilities.get_test_data import get_test_data

test_data = get_test_data("Test_Data/api_test_data.yaml")


@pytest.mark.api
class TestAPI:

    def test_01_verify_valid_login(self, auth_service, logger):
        logger.info("Test Started: Verify valid login")
        response = auth_service.login(
            test_data["user_data"]["valid_username"],
            test_data["user_data"]["valid_password"]
        )

        assert response.status_code == 200, \
            f"Test Failed: Expected status 200, got {response.status_code}"
        assert "accessToken" in response.json(), \
            "Test Failed: accessToken not found in login response"
        logger.info("Test Passed: Verified valid login")

    def test_02_verify_invalid_login(self, auth_service, logger):
        logger.info("Test Started: Verify invalid login")
        response = auth_service.login(
            test_data["user_data"]["invalid_username"],
            test_data["user_data"]["invalid_password"]
        )

        assert response.status_code == 400, \
            f"Test Failed: Invalid login should return 400, got {response.status_code}"
        logger.info("Test Passed: Verified invalid login")

    def test_03_verify_auth_user_without_token(self, user_api, logger):
        logger.info("Test Started: Verify auth user without token")
        response = user_api.get_current_user()

        assert response.status_code == 401, \
            f"Test Failed: Expected 401 Unauthorized, got {response.status_code}"
        logger.info("Test Passed: Verified auth user without token")

    def test_04_verify_auth_user_with_token(self, auth_service, user_api, logger):
        logger.info("Test Started: Verify auth user with token")
        login_response = auth_service.login(
            test_data["user_data"]["valid_username"],
            test_data["user_data"]["valid_password"]
        )

        assert login_response.status_code == 200, \
            f"Test Failed: Login expected 200, got {login_response.status_code}"

        response = user_api.get_current_user()

        assert response.status_code == 200, \
            f"Test Failed: Get current user expected 200, got {response.status_code}"
        assert "id" in response.json(), \
            "Test Failed: 'id' field missing in user response"
        logger.info("Test Passed: Verified auth user with token")

    def test_05_verify_get_all_users(self, user_api, logger):
        logger.info("Test Started: Verify get all users")
        response = user_api.get_all_users()

        assert response.status_code == 200, \
            f"Test Failed: Expected 200, got {response.status_code}"
        assert len(response.json().get("users", [])) > 0, \
            "Test Failed: User list is empty or missing"
        logger.info("Test Passed: Verified get all users")

    def test_06_verify_get_user_by_valid_id(self, user_api, logger):
        logger.info("Test Started: Verify get user by valid id")
        response = user_api.get_user_by_id(1)

        assert response.status_code == 200, \
            f"Test Failed: Expected 200, got {response.status_code}"
        assert response.json().get("id") == 1, \
            f"Test Failed: Expected user id 1, got {response.json().get('id')}"
        logger.info("Test Passed: Verified get user by valid id")

    def test_07_verify_get_user_by_invalid_id(self, user_api, logger):
        logger.info("Test Started: Verify get user by invalid id")
        response = user_api.get_user_by_id(9999)

        assert response.status_code in [200, 404], \
            f"Test Failed: Unexpected status code {response.status_code} for invalid user id"
        logger.info("Test Passed: Verified get user by invalid id")

    def test_08_verify_create_user(self, user_api, logger):
        logger.info("Test Started: Verify create user")
        payload = {
            "firstName": test_data["user_data"]["new_user_firstname"],
            "lastName": test_data["user_data"]["new_user_lastname"]
        }

        response = user_api.create_user(payload)

        assert response.status_code == 201, \
            f"Test Failed: User creation expected 201, got {response.status_code}"
        assert response.json().get("firstName") == payload["firstName"], \
            f"Test Failed: First name mismatch, expected {payload['firstName']}, got {response.json().get('firstName')}"
        logger.info("Test Passed: Verified create user")

    def test_09_verify_update_user(self, user_api, logger):
        logger.info("Test Started: Verify update user")
        payload = {
            "firstName": test_data["user_data"]["new_user_update_firstname"]
        }

        response = user_api.update_user(1, payload)

        assert response.status_code == 200, \
            f"Test Failed: User update expected 200, got {response.status_code}"
        assert response.json().get("firstName") == payload["firstName"], \
            f"Test Failed: Update failed, expected firstName {payload['firstName']}, got {response.json().get('firstName')}"
        logger.info("Test Passed: Verified update user")

    def test_10_verify_delete_user(self, user_api, logger):
        logger.info("Test Started: Verify delete user")
        response = user_api.delete_user(1)

        assert response.status_code == 200, \
            f"Test Failed: User delete expected 200, got {response.status_code}"
        assert response.json().get("isDeleted") is True, \
            "Test Failed: User was not deleted successfully"
        logger.info("Test Passed: Verified delete user")