import React, { useState, useEffect } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Container,
  Grid,
  Card,
  CardContent,
  CardMedia,
  Typography,
  Button,
  Box,
  TextField,
  MenuItem,
} from '@mui/material';
import axios from 'axios';

const categories = [
  { value: 'programming', label: 'برمجة' },
  { value: 'design', label: 'تصميم' },
  { value: 'marketing', label: 'تسويق' },
  { value: 'business', label: 'أعمال' },
];

const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [category, setCategory] = useState('');

  useEffect(() => {
    fetchCourses();
  }, [category]);

  const fetchCourses = async () => {
    try {
      setLoading(true);
      const url = category
        ? `http://localhost:8000/api/courses/?category=${category}`
        : 'http://localhost:8000/api/courses/';
      const response = await axios.get(url);
      setCourses(response.data);
      setError('');
    } catch (err) {
      setError('حدث خطأ أثناء جلب الدورات');
    }
    setLoading(false);
  };

  const handleCategoryChange = (event) => {
    setCategory(event.target.value);
  };

  if (loading) {
    return (
      <Container>
        <Typography>جاري التحميل...</Typography>
      </Container>
    );
  }

  if (error) {
    return (
      <Container>
        <Typography color="error">{error}</Typography>
      </Container>
    );
  }

  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          الدورات المتاحة
        </Typography>
        <TextField
          select
          label="التصنيف"
          value={category}
          onChange={handleCategoryChange}
          sx={{ minWidth: 200, mb: 4 }}
        >
          <MenuItem value="">الكل</MenuItem>
          {categories.map((option) => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </TextField>
        <Grid container spacing={4}>
          {courses.map((course) => (
            <Grid item key={course.id} xs={12} sm={6} md={4}>
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
          ))}
        </Grid>
      </Box>
    </Container>
  );
};

export default CourseList; 