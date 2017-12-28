
uniform mat4 uModelMatrix;
uniform mat4 uViewMatrix;
uniform mat4 uProjectionMatrix;
uniform mat3 uNormalMatrix;
uniform vec3 uLightDirection;

varying out float intensity;

in vec4 position;
in vec3 normal;

void main() 
{ 
    vec3 l_dir = normalize(uLightDirection);
    vec3 n = normalize(uNormalMatrix*normal);
    intensity = max(dot(n, l_dir), 0.0);

    gl_Position = uProjectionMatrix * uViewMatrix * uModelMatrix * position;
}