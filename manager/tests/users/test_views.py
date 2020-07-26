from flask import url_for


class TestUsersPages(object):

    def test_login_page(self, client):
        """ Login users should respond with a success 200. """

        response = client.get(url_for('users.login'))
        assert response.status_code == 200

    def test_register_page(self, client):
        """ Register users should respond with a success 200. """

        response = client.get(url_for('users.register'))
        assert response.status_code == 200
