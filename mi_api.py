from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

app = Flask(__name__)

with open('api_doc.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)
    print (yaml.dump_all(prime_service['servers'], explicit_start=True))
print(prime_service['servers'])

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'localhost:5000'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Swagger API Python",
        'body': yaml.dump_all(prime_service['servers'], explicit_start=True)
    },
     oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #'clientId': "your-client-id",
       #'clientSecret': "your-client-secret-if-required",
        #'realm': "your-realms",
       #'appName': "your-app-name",
        #'scopeSeparator': " ",
        #'additionalQueryStringParams': {'test': "hello"}
     }
)

app.register_blueprint(swaggerui_blueprint)

app.run()

# Now point your browser to localhost:5000/api/docs/