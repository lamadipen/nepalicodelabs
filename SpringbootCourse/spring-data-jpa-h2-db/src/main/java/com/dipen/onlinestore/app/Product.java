package com.dipen.onlinestore.app;

public class Product {
    private int id;
    private String name;
    private double price;
    private int qty;
    private String brand;

    public void setId(int id){
        this.id = id;
    }

    public int getId() {
        return this.id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQty() {
        return qty;
    }

    public void setQty(int qty) {
        this.qty = qty;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }




}
