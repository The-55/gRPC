import grpc
import itertools
import time
import weather_pb2
import weather_pb2_grpc

class WeatherClient:
    def __init__(self):
        # Liste des serveurs disponibles
        self.servers = ['localhost:50051', 'localhost:50052']
        # Créer un cycle infini pour le round-robin
        self.server_cycle = itertools.cycle(self.servers)
        
    def get_temperature(self, city):
        # Sélectionner le prochain serveur dans le cycle
        server_address = next(self.server_cycle)
        
        try:
            # Créer le canal de communication et le stub
            channel = grpc.insecure_channel(server_address)
            stub = weather_pb2_grpc.WeatherServiceStub(channel)
            
            # Créer la requête
            request = weather_pb2.CityRequest(city=city)
            
            # Envoyer la requête et recevoir la réponse
            response = stub.GetTemperature(request)
            
            # Afficher le résultat
            server_num = "1" if server_address.endswith('50051') else "2"
            print(f"📤 Requête → Serveur {server_num} ({server_address}) → {response.city}: {response.temperature}°C")
            
            return response
            
        except grpc.RpcError as e:
            print(f"❌ Erreur de connexion au serveur {server_address}: {e}")
            return None

def main():
    client = WeatherClient()
    city = "Tunis"
    
    print("🌍 Début des requêtes de température...")
    print("=" * 50)
    
    # Envoyer 6 requêtes pour démontrer le load balancing
    for i in range(1, 7):
        print(f"\n🔍 Requête {i}:")
        client.get_temperature(city)
        time.sleep(1)  # Pause d'une seconde entre les requêtes

if __name__ == '__main__':
    main()