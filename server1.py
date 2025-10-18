import grpc
from concurrent import futures
import time
import weather_pb2
import weather_pb2_grpc

class WeatherServiceServicer(weather_pb2_grpc.WeatherServiceServicer):
    def GetTemperature(self, request, context):
        city = request.city
        print(f"🔵 Serveur 1 - Requête reçue pour la ville: {city}")
        
        # Toujours retourner 25.0°C pour le Serveur 1
        return weather_pb2.TemperatureResponse(
            city=city,
            temperature=25.0
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(
        WeatherServiceServicer(), server
    )
    
    # Serveur 1 écoute sur le port 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    print("🚀 Serveur 1 démarré sur le port 50051")
    
    try:
        while True:
            time.sleep(86400)  # 24 heures
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()