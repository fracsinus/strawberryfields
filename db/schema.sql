/* TODO: add name, etc. */
CREATE TABLE "artists" (
    "id" serial PRIMARY KEY,
    "email" text UNIQUE NOT NULL,
    "pw_hash" text NOT NULL,
    "access_token" text UNIQUE,
    "access_token_created_at" timestamp with time zone,
    "access_token_expires_at" timestamp with time zone,
    "created_at" timestamp with time zone NOT NULL
);

/* TODO: add name, etc. */
CREATE TABLE "companies" (
    "id" serial PRIMARY KEY,
    "email" text UNIQUE,
    "pw_hash" text NOT NULL,
    "access_token" text UNIQUE,
    "access_token_created_at" timestamp with time zone,
    "access_token_expires_at" timestamp with time zone,
    "created_at" timestamp with time zone NOT NULL
);

CREATE TABLE "music" (
    "id" serial PRIMARY KEY,
    "title" text NOT NULL,
    "filename" text NOT NULL,
    "artist_id" int NOT NULL REFERENCES "artists" ("id") ON DELETE CASCADE,
    "checksum" text NOT NULL,
    "created_at" timestamp with time zone NOT NULL,
    UNIQUE ("artist_id", "checksum")
);
CREATE INDEX ON "music" ("artist_id");

CREATE TABLE "pitching" (
    "music_id" int REFERENCES "music" ("id") ON DELETE CASCADE,
    "company_id" int REFERENCES "companies" ("id") ON DELETE CASCADE,
    "created_at" timestamp with time zone NOT NULL,
    PRIMARY KEY ("music_id", "company_id")
);
