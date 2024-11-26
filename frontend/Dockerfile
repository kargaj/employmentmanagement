FROM node:20

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy project files
COPY . .

EXPOSE 3000
