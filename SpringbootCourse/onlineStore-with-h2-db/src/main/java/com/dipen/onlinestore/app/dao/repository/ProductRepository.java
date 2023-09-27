package com.dipen.onlinestore.app.dao.repository;

import com.dipen.onlinestore.app.dao.entity.ProductEntity;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ProductRepository extends CrudRepository<ProductEntity, Integer> {

    ProductEntity findById(int id);

    List<ProductEntity> findByName(int id);

}
