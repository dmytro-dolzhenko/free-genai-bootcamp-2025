package com.langportal.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import javax.sql.DataSource;
import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

@Configuration
public class DatabaseConfig {

    @Bean
    public DataSource dataSource() {
        // Get the project root directory
        String projectRoot = System.getProperty("user.dir");
        String dbPath = Paths.get(projectRoot, "words.db").toString();

        // Create database file if it doesn't exist
        File dbFile = new File(dbPath);
        if (!dbFile.exists()) {
            try {
                dbFile.createNewFile();
                // Set read/write permissions
                dbFile.setWritable(true, false);
                dbFile.setReadable(true, false);
            } catch (Exception e) {
                throw new RuntimeException("Failed to create database file: " + e.getMessage(), e);
            }
        }

        // Configure the data source
        DriverManagerDataSource dataSource = new DriverManagerDataSource();
        dataSource.setDriverClassName("org.sqlite.JDBC");
        dataSource.setUrl("jdbc:sqlite:" + dbPath);

        return dataSource;
    }
}
