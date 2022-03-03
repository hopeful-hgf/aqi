--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5 (Raspbian 13.5-0+deb11u1)
-- Dumped by pg_dump version 13.5 (Raspbian 13.5-0+deb11u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: gzrecord2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.gzrecord2 (
    aqi real,
    aqitime timestamp without time zone,
    aqi_ real,
    co real,
    co_24h real,
    co_iaqi real,
    displayname character varying(15),
    dwcode character varying(7),
    dwname character varying(15),
    msg character varying(255),
    no2 real,
    no2_24h real,
    no2_iaqi real,
    o3 real,
    o3_24h real,
    o3_8h real,
    o3_8h_24h real,
    o3_8h_iaqi real,
    o3_iaqi real,
    pm10 real,
    pm10_24h real,
    pm10_iaqi real,
    pm2_5 real,
    pm2_5_24h real,
    pm2_5_iaqi real,
    primarywrw character varying(23),
    primary_ character varying(23),
    quality character varying(7),
    quality_ character varying(7),
    so2 real,
    so2_24h real,
    so2_iaqi real,
    stcode character varying(7),
    stname character varying(7),
    x real,
    y real,
    _nullflags character varying(7)
);


ALTER TABLE public.gzrecord2 OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

