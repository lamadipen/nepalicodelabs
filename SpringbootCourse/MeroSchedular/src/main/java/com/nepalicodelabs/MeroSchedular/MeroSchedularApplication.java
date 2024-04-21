package com.nepalicodelabs.MeroSchedular;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class MeroSchedularApplication {

	public static void main(String[] args) {
		SpringApplication.run(MeroSchedularApplication.class, args);
	}

}
