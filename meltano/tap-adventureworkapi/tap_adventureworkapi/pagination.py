from singer_sdk.pagination import BaseOffsetPaginator


class AdventureWorkOffsetPaginator(BaseOffsetPaginator):
    def has_more(self, response):
        json_response = response.json()
        data = json_response.get("data", [])

        if not data:
            return False

        return True
