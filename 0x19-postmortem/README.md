Postmortem: Service Outage Due to Database Replication Lag

Issue Summary
Duration: August 10, 2024, 14:35 to 15:50 UTC (1 hour 15 minutes)
Impact: 40% of users experienced significant delays in data retrieval from our core service. Users reported slow page load times, and some actions, like updating their profiles and posting content, either timed out or resulted in errors.
Root Cause: The primary issue was a lag in database replication caused by an unexpected spike in write operations, which overwhelmed the replication process.

Timeline
14:35 UTC: Monitoring alert triggered due to a sharp increase in API response times.
14:37 UTC: On-call engineer reviewed logs and identified the slow database queries as the immediate cause.
14:40 UTC: Initial assumption was a sudden surge in traffic; traffic management measures were taken, including temporarily rate-limiting certain API endpoints.
14:45 UTC: Further investigation showed that traffic levels were normal; traffic rate-limiting did not resolve the issue.
14:50 UTC: Database team escalated the issue as replication lag was discovered. Primary database reads were delayed due to replication queues.
15:00 UTC: Misleading investigation suggested possible faulty configuration in the load balancer, leading to a brief diversion of resources.
15:15 UTC: After ruling out network issues and reviewing logs, the team focused on the replication processes.
15:30 UTC: Database team identified a large batch job, triggered unexpectedly, as the source of high write operations, causing the lag.
15:40 UTC: The batch job was canceled, and replication processes began to catch up.
15:50 UTC: System stabilized; response times returned to normal, and affected users reported restored service.

Root Cause and Resolution
The outage was caused by a replication lag in the primary database. An automated batch job, intended for non-peak hours, was inadvertently triggered during peak usage. This batch job resulted in an overwhelming number of write operations, causing replication delays across multiple read replicas. The primary database became overloaded with pending write operations, leading to slow read responses and impacting user experience.
The resolution involved canceling the batch job and allowing the replication queues to clear. The database then resumed normal operations, restoring data consistency and resolving the lag.

Corrective and Preventative Measures
Improvements Needed:
Fine-tuning the scheduling and monitoring of automated batch jobs.
Implementing stricter rate limits on write-heavy operations during peak hours.
Enhancing alerting systems to distinguish between traffic-related slowdowns and database replication issues.
Task List:
Reschedule batch jobs to strictly off-peak hours with a manual override system.
Add replication lag monitoring with proactive alerts and thresholds.
Configure a fallback system to temporarily route critical reads to the primary database in case of replication delays.
Conduct a review of database write throughput and optimize high-write query patterns.
Establish a dedicated playbook for replication-related incidents, reducing time spent on misdirected debugging path.

