package com.dipen.onlinestore.app.service;

import com.dipen.onlinestore.app.Product;
import com.dipen.onlinestore.app.dao.entity.ProductEntity;

import java.util.List;

public interface ProductService {
    List<Product> getAllProducts();
    ProductEntity saveProductEntity(Product product);

    Product getProductById(int id);

    void deleteProduct(int id);
}
