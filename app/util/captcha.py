import requests

from app.settings import AppConfig

class Captcha():
    def verify(self, token : str) -> bool:
        import requests
        """Verify a recaptcha request, return True if valid False otherwise"""
        formattedUrl = "https://www.google.com/recaptcha/api/siteverify"
        try:
            r = requests.post(formattedUrl, json={"secret":AppConfig.RECAPTCHA_SECRET, "response":token}, timeout=300)
            resp_json = r.json()
            if 'success' in resp_json and resp_json['success']:
                return True
            return False
        except requests.exceptions.RequestException:
            return False