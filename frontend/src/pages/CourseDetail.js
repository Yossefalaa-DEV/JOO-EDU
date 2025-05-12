import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import {
  Container,
  Grid,
  Typography,
  Box,
  Card,
  CardContent,
  CardMedia,
  Button,
  TextField,
  Alert,
  List,
  ListItem,
  ListItemText,
  Divider,
} from '@mui/material';
import axios from 'axios';
import { useAuth } from '../contexts/AuthContext';

const CourseDetail = () => {
  const { id } = useParams();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [activationCode, setActivationCode] = useState('');
  const [videoError, setVideoError] = useState('');
  const { user } = useAuth();

  useEffect(() => {
    fetchCourse();
  }, [id]);

  const fetchCourse = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`http://localhost:8000/api/courses/${id}/`);
      setCourse(response.data);
      setError('');
    } catch (err) {
      setError('حدث خطأ أثناء جلب تفاصيل الدورة');
    }
    setLoading(false);
  };

  const handleActivationCodeSubmit = async (videoId) => {
    try {
      setVideoError('');
      const response = await axios.post('http://localhost:8000/api/auth/validate-code/', {
        code: activationCode,
      });
      if (response.data.valid) {
        // يمكنك هنا إضافة منطق لعرض الفيديو
        window.open(`http://localhost:8000/api/courses/videos/${videoId}/?code=${activationCode}`, '_blank');
      } else {
        setVideoError(response.data.error);
      }
    } catch (err) {
      setVideoError('حدث خطأ أثناء التحقق من كود التفعيل');
    }
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

  if (!course) {
    return (
      <Container>
        <Typography>لم يتم العثور على الدورة</Typography>
      </Container>
    );
  }

  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <Grid container spacing={4}>
          <Grid item xs={12} md={8}>
            <Card>
              <CardMedia
                component="img"
                height="300"
                image={course.image || 'https://via.placeholder.com/800x300'}
                alt={course.title}
              />
              <CardContent>
                <Typography variant="h4" component="h1" gutterBottom>
                  {course.title}
                </Typography>
                <Typography variant="body1" paragraph>
                  {course.description}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={4}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  محتوى الدورة
                </Typography>
                <List>
                  {course.videos.map((video, index) => (
                    <React.Fragment key={video.id}>
                      <ListItem>
                        <ListItemText
                          primary={video.title}
                          secondary={`المدة: ${video.duration || 'غير محدد'}`}
                        />
                        {user ? (
                          <Box>
                            <TextField
                              size="small"
                              label="كود التفعيل"
                              value={activationCode}
                              onChange={(e) => setActivationCode(e.target.value)}
                              sx={{ mr: 1 }}
                            />
                            <Button
                              variant="contained"
                              onClick={() => handleActivationCodeSubmit(video.id)}
                            >
                              تشغيل
                            </Button>
                          </Box>
                        ) : (
                          <Button
                            variant="contained"
                            component="a"
                            href="/login"
                          >
                            تسجيل الدخول
                          </Button>
                        )}
                      </ListItem>
                      {index < course.videos.length - 1 && <Divider />}
                    </React.Fragment>
                  ))}
                </List>
                {videoError && (
                  <Alert severity="error" sx={{ mt: 2 }}>
                    {videoError}
                  </Alert>
                )}
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default CourseDetail; 