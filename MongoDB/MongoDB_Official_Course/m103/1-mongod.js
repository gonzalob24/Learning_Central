// YAML file
storage: dbPath: "/data/db";
systemLog: path: "/data/log/mongod.log";
destination: "file";
replication: replSetName: M103;
net: bindIp: "127.0.0.1,192.168.103.100";
tls: mode: "requireTLS";
certificateKeyFile: "/etc/tls/tls.pem";
CAFile: "/etc/tls/TLSCA.pem";
security: keyFile: "/data/keyfile";
processManagement: fork: true;

// connect to a running instance of mongod
// mongo --port 27000 -u m103-admin -p m103-pass --authenticationDatabase admin
// create this user on the admin DB
// use admin
const user = db.createUser({
	user: "m103-application-user",
	pwd: "m103-application-pass",
	roles: [{ db: "applicationData", role: "readWrite" }],
});

// mongoimport
// mongoimport --port 27000 -u "m103-application-user" -p "m103-application-pass" --authenticationDatabase admin -d applicationData -c products --file "/dataset/products.json"

// sudo mongod --auth --dbpath /Users/gonzalobetancourt/mongodb/data --logpath /Users/gonzalobetancourt/mongodb/logs/mongo.log --fork

// create a user
db.createUser({
	user: "name",
	pwd: "password",
	roles: [{ role: "type", db: "database" }],
});
db.auth(user, pwd);
db.logout();

// For testing generate ssl cert
// sudo openssl req -newkey rsa:2048 -new -x509 -days 365 -nodes -out mongodb-cert.crt -keyout mongodb-cert.key

// concat the certificate and private key to a .pem file
// cat mongodb-cert.key mongodb-cert.crt > mongodb.pem

/**
 Country Name (2 letter code) []:USA
string is too long, it needs to be less than  2 bytes long
Country Name (2 letter code) []:US 
State or Province Name (full name) []:Michigan
Locality Name (eg, city) []:Utica
Organization Name (eg, company) []:Student
Organizational Unit Name (eg, section) []:Dev
// localhost is for dev purposes
Common Name (eg, fully qualified host name) []:localhost or address of server when deploying
Email Address []:me@gmail.com
 */
