USE [master]
GO
/****** Object:  Database [Java]    Script Date: 21.06.2024 14:21:46 ******/
CREATE DATABASE [Java]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Java', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\Java.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Java_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\Java_log.ldf' , SIZE = 73728KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [Java] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Java].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Java] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Java] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Java] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Java] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Java] SET ARITHABORT OFF 
GO
ALTER DATABASE [Java] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Java] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Java] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Java] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Java] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Java] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Java] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Java] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Java] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Java] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Java] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Java] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Java] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Java] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Java] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Java] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Java] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Java] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Java] SET  MULTI_USER 
GO
ALTER DATABASE [Java] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Java] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Java] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Java] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Java] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Java] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [Java] SET QUERY_STORE = ON
GO
ALTER DATABASE [Java] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Java]
GO
/****** Object:  Table [dbo].[Eqipment]    Script Date: 21.06.2024 14:21:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Eqipment](
	[ID] [int] NOT NULL,
	[NV] [nvarchar](50) NULL,
	[ProductLine] [nvarchar](50) NULL,
	[Material] [nvarchar](50) NULL,
	[Description] [nvarchar](500) NULL,
	[ProjectPrice] [decimal](10, 2) NULL,
	[BasicDiscount] [decimal](10, 2) NULL,
	[RecomendedRetailPrice] [decimal](10, 2) NULL,
	[Comments] [nvarchar](500) NULL
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [Java] SET  READ_WRITE 
GO
