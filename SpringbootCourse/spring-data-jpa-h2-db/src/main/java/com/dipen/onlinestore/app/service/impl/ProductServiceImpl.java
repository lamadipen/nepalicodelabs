package com.dipen.onlinestore.app.service.impl;

import com.dipen.onlinestore.app.Product;
import com.dipen.onlinestore.app.dao.entity.ProductEntity;
import com.dipen.onlinestore.app.dao.repository.ProductRepository;
import com.dipen.onlinestore.app.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class ProductServiceImpl implements ProductService {

    @Autowired
    private ProductRepository productRepository;

    @Override
    public List<Product> getAllProducts() {
        List<Product> products = new ArrayList<>();
        Iterable<ProductEntity> productEntityIterable = productRepository.findAll();

        productEntityIterable.forEach(productEntity -> {
            Product product = new Product();
            product.setId(productEntity.getId());
            product.setName(productEntity.getName());
            product.setBrand(productEntity.getBrand());
            product.setPrice(productEntity.getPrice());
            product.setQty(productEntity.getQyt());
            products.add(product);
        });

        return products;
    }

    @Override
    public ProductEntity saveProductEntity(Product product) {
        ProductEntity productEntity = new ProductEntity();
        productEntity.setName(product.getName());
        productEntity.setPrice(product.getPrice());
        productEntity.setQyt(product.getQty());
        productEntity.setBrand(product.getBrand());

        return productRepository.save(productEntity);
    }

    @Override
    public Product getProductById(int id) {
        Optional<ProductEntity> optionalProductEntity = productRepository.findById(id);

        ProductEntity productEntity = optionalProductEntity.get();
        Product product = new Product();
        product.setId(productEntity.getId());
        product.setName(productEntity.getName());
        product.setPrice(productEntity.getPrice());
        product.setQty(productEntity.getQyt());

        return product;
    }

    @Override
    public void deleteProduct(int id) {
        productRepository.deleteById(id);
    }
}
