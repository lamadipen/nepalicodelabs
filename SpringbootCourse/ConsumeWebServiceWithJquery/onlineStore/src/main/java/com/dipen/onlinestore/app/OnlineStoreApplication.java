package com.dipen.onlinestore.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
@RestController
public class OnlineStoreApplication {

	List<Product> products = new ArrayList<>();

	public static void main(String[] args) {
		SpringApplication.run(OnlineStoreApplication.class, args);
	}

	@Configuration
	@EnableWebMvc
	public class WebConfig implements WebMvcConfigurer{
		public void addCorsMappings(CorsRegistry corsRegistry) {
			corsRegistry.addMapping("/**");
		}
	}

	@CrossOrigin(origins = "*")
	@GetMapping("/welcome")
	public String welcome(){
		return "Welcome to online store";
	}

	@GetMapping("/welcome/{username}/{age}")
	public String welcomeWithUser(@PathVariable String username, @PathVariable int age){
		return "Welcome to online store: " + username + "with age " + age;
	}

	@GetMapping("/hello")
	public String helloWithQueryParameter(@RequestParam String username, @RequestParam(name = "userage") int age){
		return "Hello : " + username + "with age " + age;
	}

	@PostMapping("/msg")
	public String getDataFromPost(@RequestBody String message) {
		return "You have sent following message in Post: " + message;
	}

	@PutMapping("/msg")
	public String getDataFromPut(@RequestBody String message) {
		return "You have sent following message in Put: " + message;
	}

	@GetMapping("/product")
	public List<Product> getAllProducts() {
		return products;
	}

	@GetMapping("/product/{id}")
	public Product getProductById(@PathVariable int id) {
		for (int i = 0; i < products.size(); i++) {
			if (products.get(i).getId() == id) {
				return products.get(i);
			}
		}
		return null;
	}

	@PostMapping("/product")
	public String createProduct(@RequestBody Product product){
		products.add(product);
		return "product added successfully";
	}

	@DeleteMapping("/product/{id}")
	public String deleteProduct(@PathVariable int id){
		for (int i = 0; i < products.size(); i++) {
			if (products.get(i).getId() == id) {
				products.remove(i);
				return "product deleted successfully";
			}
		}
		return "product with id not found";
	}

}
