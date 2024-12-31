# Stage 1: Build frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend

# Copy frontend files
COPY frontend/package*.json ./
RUN npm install --force

COPY frontend/ .

ENV NEXT_PUBLIC_API_URL=https://state.sshh.io

RUN npm run build

# Stage 2: Build backend and serve frontend
FROM python:3.11-slim
WORKDIR /app

# Install Node.js and Nginx
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Copy backend requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# Copy backend code
COPY backend/ .

# Copy built frontend from previous stage
COPY --from=frontend-builder /app/frontend/.next /app/frontend/.next
COPY --from=frontend-builder /app/frontend/public /app/frontend/public
COPY --from=frontend-builder /app/frontend/package*.json /app/frontend/
COPY --from=frontend-builder /app/frontend/next.config.mjs /app/frontend/

# Install frontend production dependencies
WORKDIR /app/frontend
RUN npm install --production --force

# Fix the nginx.conf copy path
COPY backend/nginx.conf /etc/nginx/nginx.conf

# Modify start script to include nginx
RUN echo '#!/bin/bash\n\
    service nginx start\n\
    cd /app/frontend && npm start & \n\
    cd /app && uvicorn main:app --host 0.0.0.0 --port 8000 --ws auto\n\
    wait' > /app/start.sh && chmod +x /app/start.sh

# Expose port 80 for Nginx
EXPOSE 80

# Set environment variables
ENV NODE_ENV=production

# Use the start script instead of direct uvicorn command
CMD ["/app/start.sh"]