FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
EXPOSE 3000

COPY ontopvpn.crt /etc/ssl/legkovpn.crt
COPY ontopvpn.key /etc/ssl/legkovpn.key
COPY ca.crt /etc/ssl/ca.crt

CMD ["nginx", "-g", "daemon off;"]
