package com.dipen.onlinestore.app.service;

import com.dipen.onlinestore.app.model.request.Product;

import java.util.List;

public interface ProductService {
    void addProduct(Product product);
    Product getProductById(int id);
    Product getProductByName(String name);

}
