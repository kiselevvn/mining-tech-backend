from src.settings.base import env

CRYPTO_CLOUD_API_KEY = env("CRYPTO_CLOUD_API_KEY", default="")
CRYPTO_CLOUD_SHOP_ID = env("CRYPTO_CLOUD_SHOP_ID", default="")

# DJOSER = {
#     # 'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
#     # 'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
#     # 'ACTIVATION_URL': '#/activate/{uid}/{token}',
#     # 'SEND_ACTIVATION_EMAIL': True,
#     'SERIALIZERS': {

#         },
# }