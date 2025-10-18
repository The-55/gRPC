import grpc
from concurrent import futures
import time
import weather_pb2
import weather_pb2_grpc

class WeatherServiceServicer(weather_pb2_grpc.WeatherServiceServicer):
    def GetTemperature(self, request, context):
        city = request.city
        print(f"🟢 Serveur 2 - Requête reçue pour la ville: {city}")
        
        # Toujours retourner 26.0°C pour le Serveur 2
        return weather_pb2.TemperatureResponse(
            city=city,
            temperature=26.0
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(
        WeatherServiceServicer(), server
    )
    
    # Serveur 2 écoute sur le port 50052
    server.add_insecure_port('[::]:50052')
    server.start()
    print("🚀 Serveur 2 démarré sur le port 50052")
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()