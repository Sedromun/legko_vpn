up:
	docker compose -f compose.dev.yaml up --build -d bot_vpn
down:
	docker compose -f compose.dev.yaml down
bot:
	docker exec -it bot_vpn bash
db:
	docker exec -it database_vpn bash
