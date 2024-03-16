package com.dipen.onlinestore.app.dao.entity;


import org.springframework.data.annotation.Id;

public class ProductEntity {
    @Id

    private String id;
    private String name;
    private double price;
    private int qty;

    private String brand;

    public void setId(String id){
        this.id = id;
    }

    public String getId() {
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

    @Override
    public String toString() {
        return "ProductEntity{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", price=" + price +
                ", qty=" + qty +
                ", brand='" + brand + '\'' +
                '}';
    }
}
