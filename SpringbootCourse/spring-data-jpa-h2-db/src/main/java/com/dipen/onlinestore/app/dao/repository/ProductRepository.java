package com.dipen.onlinestore.app.dao.repository;

import com.dipen.onlinestore.app.dao.entity.ProductEntity;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends CrudRepository<ProductEntity, Integer> {

}
