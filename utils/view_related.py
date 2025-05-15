    
class SubcriptionListView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 
class SubscribeApiView(APIView):
    def post(self, request):
        serializer = SubscribeSerializer(data= request.data)
        if serializer.is_valid():
            subscription = serializer.save()
            return Response(SubscriptionSerializer(subscription).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubcriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer


class SubcriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionRetrieveView(generics.RetrieveAPIView):
    serializer_class = SubscriptionSerializer

    def get_object(self):
        """
        Fetch the object to be serialized and returned in GET.
        """
        user = self.request.user
        try:
            return Subscription.objects.get(subscriber__user=user)
        except Subscription.DoesNotExist:
            raise NotFound('Subscription not found')
   

class SubscriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Called after serializer.is_valid() and before saving to DB.
        Override this to customize how objects are saved.
        """
        self.subscription = serializer.save()
    
    def create(self, request, *args, **kwargs):
        """
        Override this to customize the full save-response flow.
        """
        response = super().create(request, *args, **kwargs)
        # Replace response.data if needed:
        response.data = SubscriptionSerializer(self.subscription).data
        return response


class SubscriptionDeleteView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    def get_object(self):
        """
        Locate the Subscription object tied to the authenticated user.
        """
        user = self.request.user
        try:
            return Subscription.objects.get(subscriber__user=user)
        except Subscription.DoesNotExist:
            raise NotFound("No active subscription found for this user.")