from channels.routing import ProtocolTypeRouter, URLRouter

import user_chat.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(
            user_chat.routing.websocket_urlpatterns
        )
})
