# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_properties_with_escaped_characters_request_body import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRequestBodyPostPropertiesWithEscapedCharactersRequestBody(ApiTestMixin, unittest.TestCase):
    """
    RequestBodyPostPropertiesWithEscapedCharactersRequestBody unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_object_with_all_numbers_is_valid_passes(self):
        content_type = 'application/json'
        # object with all numbers is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo\nbar":
                        1,
                    "foo\"bar":
                        1,
                    "foo\\bar":
                        1,
                    "foo\rbar":
                        1,
                    "foo\tbar":
                        1,
                    "foo\fbar":
                        1,
                }
            )
            body = post.SchemaForRequestBodyApplicationJson._from_openapi_data(
                payload,
                _configuration=self._configuration
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
                content_type=content_type
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self._configuration.host + '/requestBody/postPropertiesWithEscapedCharactersRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_object_with_strings_is_invalid_fails(self):
        content_type = 'application/json'
        # object with strings is invalid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo\nbar":
                        "1",
                    "foo\"bar":
                        "1",
                    "foo\\bar":
                        "1",
                    "foo\rbar":
                        "1",
                    "foo\tbar":
                        "1",
                    "foo\fbar":
                        "1",
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.SchemaForRequestBodyApplicationJson._from_openapi_data(
                    payload,
                    _configuration=self._configuration
                )
                self.api.post(body=body)




if __name__ == '__main__':
    unittest.main()