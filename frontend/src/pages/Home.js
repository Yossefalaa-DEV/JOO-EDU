import React, { useState, useEffect } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Container,
  Box,
  Typography,
  Button,
  Grid,
  Card,
  CardContent,
  CardMedia,
} from '@mui/material';
import axios from 'axios';

const Home = () => {
  const [featuredCourses, setFeaturedCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchFeaturedCourses();
  }, []);

  const fetchFeaturedCourses = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/courses/');
      setFeaturedCourses(response.data.slice(0, 3)); // عرض أول 3 دورات
      setLoading(false);
    } catch (error) {
      console.error('Error fetching courses:', error);
      setLoading(false);
    }
  };

  return (
    <Box>
      {/* Hero Section */}
      <Box
        sx={{
          bgcolor: 'primary.main',
          color: 'white',
          py: 8,
          mb: 6,
        }}
      >
        <Container maxWidth="md">
          <Typography
            component="h1"
            variant="h2"
            align="center"
            gutterBottom
          >
            مرحباً بك في JOO EDU
          </Typography>
          <Typography variant="h5" align="center" paragraph>
            منصة تعليمية متكاملة تقدم دورات عالية الجودة في مختلف المجالات
          </Typography>
          <Box sx={{ mt: 4, textAlign: 'center' }}>
            <Button
              component={RouterLink}
              to="/courses"
              variant="contained"
              color="secondary"
              size="large"
              sx={{ mx: 1 }}
            >
              تصفح الدورات
            </Button>
            <Button
              component={RouterLink}
              to="/register"
              variant="outlined"
              color="inherit"
              size="large"
              sx={{ mx: 1 }}
            >
              إنشاء حساب
            </Button>
          </Box>
        </Container>
      </Box>

      {/* Featured Courses Section */}
      <Container>
        <Typography variant="h4" component="h2" gutterBottom align="center">
          الدورات المميزة
        </Typography>
        <Grid container spacing={4} sx={{ mt: 2 }}>
          {loading ? (
            <Typography>جاري التحميل...</Typography>
          ) : (
            featuredCourses.map((course) => (
              <Grid item key={course.id} xs={12} md={4}>
                <Card
                  sx={{
                    height: '100%',
                    display: 'flex',
                    flexDirection: 'column',
                  }}
                >
                  <CardMedia
                    component="img"
                    height="140"
                    image={course.image || 'https://via.placeholder.com/300x140'}
                    alt={course.title}
                  />
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="h5" component="h2">
                      {course.title}
                    </Typography>
                    <Typography>{course.description}</Typography>
                  </CardContent>
                  <Box sx={{ p: 2 }}>
                    <Button
                      component={RouterLink}
                      to={`/courses/${course.id}`}
                      variant="contained"
                      fullWidth
                    >
                      عرض الدورة
                    </Button>
                  </Box>
                </Card>
              </Grid>
            ))
          )}
        </Grid>
      </Container>
    </Box>
  );
};

export default Home; 