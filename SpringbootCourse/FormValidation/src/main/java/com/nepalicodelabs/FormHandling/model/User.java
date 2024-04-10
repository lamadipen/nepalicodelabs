package com.nepalicodelabs.FormHandling.model;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public class User {
    @NotNull
    @Size(min=2, max=30)
    private String name;

    @NotNull
    @Size(min=6, max=30)
    @Email
    private String email;

    @NotNull
    @Min(value = 18, message = "Age must be greater that 18 ")
    private int age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
