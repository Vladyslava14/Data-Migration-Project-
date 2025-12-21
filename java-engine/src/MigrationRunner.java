package com.migration;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class MigrationRunner {

    public static void main(String[] args) {
        System.out.println("Java Migration Engine started");

        try {
            // команда для Windows
            String command = "python etl_pipeline.py";

            Process process = Runtime.getRuntime().exec(command);

            BufferedReader reader =
                    new BufferedReader(new InputStreamReader(process.getInputStream()));

            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("PYTHON >> " + line);
            }

            int exitCode = process.waitFor();

            if (exitCode == 0) {
                System.out.println("ETL completed successfully via Java Engine");
            } else {
                System.out.println("ETL finished with errors. Exit code: " + exitCode);
            }

        } catch (Exception e) {
            System.out.println("Migration Error: " + e.getMessage());
        }
    }
}
