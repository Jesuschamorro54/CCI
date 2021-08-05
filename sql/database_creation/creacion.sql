-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cci
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cci
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cci` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `cci` ;

-- -----------------------------------------------------
-- Table `cci`.`adress`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`adress` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(10) NULL DEFAULT NULL,
  `carrera` VARCHAR(10) NULL DEFAULT NULL,
  `diagonal` VARCHAR(10) NULL DEFAULT NULL,
  `transversal` VARCHAR(10) NULL DEFAULT NULL,
  `numero` INT NULL DEFAULT NULL,
  `barrio` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`area`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`area` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NULL DEFAULT NULL,
  `descriptions` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`cargos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`cargos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL DEFAULT NULL,
  `nivel` INT NULL DEFAULT NULL,
  `descriptions` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`proveedores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NULL DEFAULT NULL,
  `telefono` BIGINT NULL DEFAULT NULL,
  `tipo` INT NULL DEFAULT NULL,
  `bodega` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`implementos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`implementos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL DEFAULT NULL,
  `belonging` INT NULL DEFAULT NULL,
  `proveedor` INT NULL DEFAULT NULL,
  `estado` INT NULL DEFAULT NULL,
  `descriptions` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `belonging` (`belonging` ASC) VISIBLE,
  INDEX `proveedor` (`proveedor` ASC) VISIBLE,
  CONSTRAINT `implementos_ibfk_1`
    FOREIGN KEY (`belonging`)
    REFERENCES `cci`.`area` (`id`),
  CONSTRAINT `implementos_ibfk_2`
    FOREIGN KEY (`proveedor`)
    REFERENCES `cci`.`proveedores` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`commodity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`commodity` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `supplier` INT NULL DEFAULT NULL,
  `implement` INT NULL DEFAULT NULL,
  `cantidad` INT NULL DEFAULT NULL,
  `valor_unico` INT NULL DEFAULT NULL,
  `valor_total` INT NULL DEFAULT NULL,
  `fecha_pedido` DATETIME NULL DEFAULT NULL,
  `fecha_recibido` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `supplier` (`supplier` ASC) VISIBLE,
  INDEX `implement` (`implement` ASC) VISIBLE,
  CONSTRAINT `commodity_ibfk_1`
    FOREIGN KEY (`supplier`)
    REFERENCES `cci`.`proveedores` (`id`),
  CONSTRAINT `commodity_ibfk_2`
    FOREIGN KEY (`implement`)
    REFERENCES `cci`.`implementos` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`empleados` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL DEFAULT NULL,
  `cargo` INT NULL DEFAULT NULL,
  `telefono` BIGINT NULL DEFAULT NULL,
  `dir` INT NULL DEFAULT NULL,
  `fecha_inicio` DATE NULL DEFAULT NULL,
  `fecha_final` DATE NULL DEFAULT NULL,
  `estado` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `cargo` (`cargo` ASC) VISIBLE,
  INDEX `dir` (`dir` ASC) VISIBLE,
  CONSTRAINT `empleados_ibfk_1`
    FOREIGN KEY (`cargo`)
    REFERENCES `cci`.`cargos` (`id`),
  CONSTRAINT `empleados_ibfk_2`
    FOREIGN KEY (`dir`)
    REFERENCES `cci`.`adress` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 203122
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`type_servicies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`type_servicies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NULL DEFAULT NULL,
  `descriptions` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`servicies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`servicies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NULL DEFAULT NULL,
  `estado` INT NULL DEFAULT NULL,
  `tipo` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `tipo` (`tipo` ASC) VISIBLE,
  CONSTRAINT `servicies_ibfk_1`
    FOREIGN KEY (`tipo`)
    REFERENCES `cci`.`type_servicies` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`mantenimiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`mantenimiento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `authorized` INT NULL DEFAULT NULL,
  `assigned` INT NULL DEFAULT NULL,
  `entity` INT NULL DEFAULT NULL,
  `programmed` DATETIME NULL DEFAULT NULL,
  `estado` INT NULL DEFAULT NULL,
  `fecha_inicio` DATETIME NULL DEFAULT NULL,
  `fecha_final` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `authorized` (`authorized` ASC) VISIBLE,
  INDEX `entity` (`entity` ASC) VISIBLE,
  CONSTRAINT `mantenimiento_ibfk_1`
    FOREIGN KEY (`authorized`)
    REFERENCES `cci`.`empleados` (`id`),
  CONSTRAINT `mantenimiento_ibfk_2`
    FOREIGN KEY (`entity`)
    REFERENCES `cci`.`servicies` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cci`.`recents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cci`.`recents` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `maintenance` INT NULL DEFAULT NULL,
  `implement` INT NULL DEFAULT NULL,
  `date` DATETIME NULL DEFAULT NULL,
  `assigned` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `maintenance` (`maintenance` ASC) VISIBLE,
  INDEX `implement` (`implement` ASC) VISIBLE,
  INDEX `assigned` (`assigned` ASC) VISIBLE,
  CONSTRAINT `recents_ibfk_2`
    FOREIGN KEY (`maintenance`)
    REFERENCES `cci`.`mantenimiento` (`id`),
  CONSTRAINT `recents_ibfk_4`
    FOREIGN KEY (`implement`)
    REFERENCES `cci`.`implementos` (`id`),
  CONSTRAINT `recents_ibfk_5`
    FOREIGN KEY (`assigned`)
    REFERENCES `cci`.`empleados` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 32
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;