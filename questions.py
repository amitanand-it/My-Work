design a Notification service –

HLD - Infrastructure
LLD - DB and API interaction

CDN (static content and for page caching purpose)

Servers 
Frontend : Nginx & Apache ( Rewrite rules if required )
Load Balancer (to handle the load/coming traffic)
Request will be sent to any backend server
Multiple backend servers 
Auto Scalable (can be on own servers, GCP, AWS etc.)
Cluster: B1, B2, B3
(Each backend server will have its own apache/nginx machine
Where required only)

Dedicated or Centralised servers List (So that any application can communicate with them in synchronised manner)
Servers: Redis (Session Management, DB, Cache)
Servers: Memcache (Caching in Memory)
Servers: RabbitMQ (Queues for streaming data like Incoming mails, Notifications, Messages)
Servers:  Master Database (for write operations) ,
               Slaves or replicas for readonly queries,
 	   pgbouncer (for load balancing at DB level)
Servers: Image Server
Servers: Elastic Search
Servers: Kibana
Servers: Payments 
Servers: Mail Servers
Servers: Log Servers





B1 -> Django , Python , DRF, modules application based
	

Notification_master
Not_Id
Template Id
Notification msg
Last updated
Generated
Last updated by

Notifications
Id
Not_id  (Ref Notification master)
Source    Mobile/Email
Sender    (ref users userid)
Status    (InProcess/Bounce)
Receiver  (ref users userid)
Extra comments
Generated 
Last updated by (ref Empid)
Last updated




Select n.status, count(*) 
from notifications n join notification_master nm on (n.Not_id = nm.Not_id) 
Where nm.template_id = 2  
group by n.status;



Users
Userid 
Username
Mobile
Extras
Valid 
Generated

ProfileMaster
Profile_id
Company_name
Address
Pan_no
Gst_no
Registered_since
Members_count
Others data
Generated
Last_updated
Updated_by

AccountProfiles
id
Profile_id
userid


MobileMaster
Mobile_key
Mobile
Verified
Verified_on
verified _by (ref employees)
Generated
Last_updated

EmailMaster
email_key
email
Verified
Verified_on
verified _by (ref employees)
Generated
Last_updated


Employees
Emp_id
Emp_name
Designation (ref designations)
Date_of_birth
Date_of_joining
Department (ref departments)
Branch  (ref branch master)
Reports_to
Generated
Last_updated
Last_updated_by (ref employees)
Mobile (ref mobile master)
Email (ref email master)
Other details

BranchMaster
Branch_id
Branch_name
area
Generated
last_updated
Last_updated_by (ref employees)

Departments
Dept_id
Department_name
Generated
Last_updated
Last_updated_by (ref employees)

Designations
Desig_id
Designation
Generated
Last_updated
Last_updated_by (ref employees)


For API Interaction
We can use Django , DRF or Fast API

Models : Database representation
Views: Writing the logic 
	(ORM , fetch or update data from DB, Application Code)
Templates: Designs View (Templates)
Settings Module: In settings need to mention 
                          root_urlconf, DB config, redis config, memcache conf











