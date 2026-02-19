#!/usr/bin/env python3
"""Create expert issues with correct labels"""

import subprocess
import time

EXPERT_ISSUES = [
    ("Build Distributed Task Queue", "081_task_queue.py", "Implement distributed task queue"),
    ("Build Message Queue System", "082_message_queue.py", "Implement message queue"),
    ("Build Load Balancer Simulator", "083_load_balancer.py", "Simulate load balancing"),
    ("Build Cache System Implementation", "084_cache_system.py", "Implement caching system"),
    ("Build Rate Limiter Service", "085_rate_limiter_service.py", "Build rate limiting service"),
    ("Build Circuit Breaker Pattern", "086_circuit_breaker.py", "Implement circuit breaker"),
    ("Build Event Sourcing System", "087_event_sourcing.py", "Implement event sourcing"),
    ("Build CQRS Implementation", "088_cqrs_impl.py", "Implement CQRS pattern"),
    ("Build Memory Profiler Tool", "089_memory_profiler.py", "Profile memory usage"),
    ("Build CPU Profiler Tool", "090_cpu_profiler.py", "Profile CPU usage"),
    ("Build Performance Benchmark Tool", "091_benchmark_tool.py", "Benchmark code performance"),
    ("Build Algorithm Optimizer", "092_algo_optimizer.py", "Optimize algorithm performance"),
    ("Build Database Query Optimizer", "093_query_optimizer.py", "Optimize database queries"),
    ("Build Caching Strategy Tool", "094_cache_strategy.py", "Implement caching strategies"),
    ("Build Password Hash Generator", "095_password_hasher.py", "Generate secure password hashes"),
    ("Build JWT Token Handler", "096_jwt_handler.py", "Handle JWT tokens"),
    ("Build Encryption Tool", "097_encryption_tool.py", "Encrypt/decrypt data"),
    ("Build Security Scanner", "098_security_scanner.py", "Scan for security issues"),
    ("Build Input Sanitizer", "099_input_sanitizer.py", "Sanitize user input"),
    ("Build Authentication System", "100_auth_system.py", "Build authentication system"),
]

for title, file, desc in EXPERT_ISSUES:
    body = f"""## Description
{desc}

## Difficulty
Expert

## File Location
exercises/1000_programs/expert/{file}

## Requirements
- [ ] Implement advanced functionality
- [ ] Handle edge cases
- [ ] Add comprehensive error handling
- [ ] Include type hints
- [ ] Add docstrings
- [ ] Write tests

## Expected Behavior
System should work correctly under various conditions.

## Acceptance Criteria
- [ ] Core functionality works
- [ ] Error handling present
- [ ] Type hints included
- [ ] Documentation complete
- [ ] Follows best practices

## Hints
- Research design patterns
- Consider scalability
- Test thoroughly

## Related Issues
Part of 250 issues initiative"""

    cmd = ["gh", "issue", "create", "--title", f"[EXPERT] {title}", "--body", body, "--label", "advanced,exercise"]
    subprocess.run(cmd, capture_output=True)
    time.sleep(3)
    print(f"✓ Created: {title}")

print("\nExpert issues created!")
