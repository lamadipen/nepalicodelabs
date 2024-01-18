package com.dipen.onlinestore.app.service.impl;

import com.dipen.onlinestore.app.dao.entity.ProductEntity;
import com.dipen.onlinestore.app.dao.repository.ProductRepository;
import com.dipen.onlinestore.app.model.request.Product;
import com.dipen.onlinestore.app.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ProductServiceImpl implements ProductService {

    @Autowired
    private ProductRepository productRepository;
    @Override
    public void addProduct(Product product) {
        ProductEntity productEntity = new ProductEntity();
        productEntity.setName(product.getName());
        productEntity.setBrand(product.getBrand());
        productEntity.setPrice(product.getPrice());
        productEntity.setQty(product.getQty());

        productRepository.save(productEntity);
    }

    @Override
    public Product getProductById(int id) {
        return null;
    }

    @Override
    public Product getProductByName(String name) {
        return null;
    }
}
