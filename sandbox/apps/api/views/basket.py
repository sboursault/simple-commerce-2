from rest_framework.views import APIView
from rest_framework.response import Response
from oscarapi.utils.loading import get_api_classes

from oscarapi.basket import operations

(  # pylint: disable=unbalanced-tuple-unpacking
    BasketSerializer,
) = get_api_classes(
    "serializers.basket",
    [
        "BasketSerializer",
    ],
)


class BasketView(APIView):
    """
    Api for retrieving a user's basket.

    GET:
    Retrieve your basket.

    DELETE:
    Delete your basket.
    """

    serializer_class = BasketSerializer

    def get(self, request, *args, **kwargs):  # pylint: disable=redefined-builtin
        basket = operations.get_basket(request)
        ser = self.serializer_class(basket, context={"request": request})
        return Response(ser.data)

    def delete(self, request, *args, **kwargs):  # pylint: disable=redefined-builtin
        basket = operations.get_basket(request)
        basket.delete()
        return Response(status=207)
