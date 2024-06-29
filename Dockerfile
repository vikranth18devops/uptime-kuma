# Use the official Node.js 18 image as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to install dependencies first
COPY package*.json ./

# Install any dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY . .

# Build the project to generate the dist directory
RUN npm run build

# Expose the port Uptime Kuma will run on
EXPOSE 3001

# Command to run the application
CMD ["node", "server/server.js"]
