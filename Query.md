Non spatial query : Get all matching country names by string

      SELECT * FROM corrected_countries WHERE "ADMIN" LIKE '% #string %'
      
Spatial query: Get all counties Intersecting with India

Approach: find the geom co-ordinates of India and the compare it to geom in the database and select the countries which intersects or touches with Indian geom coordinates

      SELECT geom FROM corrected_countries  ST_Touches(SELECT geom from corrected_countries WHERE "ADMIN" = 'India' , corrected_countries.geom);
