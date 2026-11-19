# First-Version Process Flow

```mermaid
flowchart TD
    A[Open workout log] --> B{Saved data readable?}
    B -->|Yes| C[Display history or empty state]
    B -->|No| D[Show recovery message; preserve stored data]
    C --> E[Enter exercise, weight, and reps]
    E --> F[Select Save set]
    F --> G{Inputs valid?}
    G -->|No| H[Show field errors; keep inputs]
    H --> E
    G -->|Yes| I[Create ID and timestamp; attempt local save]
    I --> J{Save succeeded?}
    J -->|No| K[Show storage error; keep inputs]
    K --> E
    J -->|Yes| L[Show confirmation and updated history]
    L --> E
    L --> M[Refresh or reopen same site]
    M --> B
```

Each entry is one set. Version 1 has no login, cloud synchronization, or separate session-management step. Recovery from unreadable data must not silently delete or replace it.
