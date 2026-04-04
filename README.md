# RoleGate Backend

**RoleGate** is a production-ready authentication and user management backend built with **Python**, **FastAPI**, and **PostgreSQL**. It implements authentication, access and refresh tokens, role-based access control (RBAC), admin controls, rate limiting, pagination, and filtering.

---

## Features

### Authentication
- User registration and login  
- JWT access tokens (15 minutes)  
- JWT refresh tokens (7 days) with rotation  
- Secure logout (refresh token invalidation)  
- Token refresh endpoint  

### User Management
- Get current logged-in user  
- Admin: get all users  
- Admin: delete user  
- Admin: force logout user  
- Admin: change user role  

### Authorization (RBAC)
- Role-based access control (user, admin)  
- Middleware/dependency for authentication and authorization  
- Admin self-protection (cannot downgrade own role)  
- Invalid role handling  

### Security and Performance
- Password hashing with **bcrypt**  
- Rate limiting on auth and admin routes  
- Centralized error handling  
- Environment-based configuration  

### Pagination and Filtering
- Paginated admin user list  
- Role-based filtering  
- Keyword search  
- Accurate record counting using filters  

---

## Tech Stack
- Python 3.11+  
- FastAPI  
- PostgreSQL  
- SQLAlchemy ORM  
- Pydantic for data validation  
- JWT (PyJWT)  
- Passlib (bcrypt)  
- Alembic for database migrations  

---

Author

Built by Ayush, focused on clean backend architecture and real-world systems.

License

MIT License
Copyright (c) 2026 Ayush

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.
