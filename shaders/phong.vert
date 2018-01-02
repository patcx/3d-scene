uniform mat4 uModelMatrix;
uniform mat4 uViewMatrix;
uniform mat4 uProjectionMatrix;
uniform mat3 uNormalMatrix;

in vec4 position;
in vec3 normal;
in vec3 diffuse;

varying out vec4 vertex;
varying out vec4 v;
varying out vec3 n;
varying out vec3 fragDiffuse;


void main() 
{ 
    fragDiffuse = diffuse;
    n = normalize(uNormalMatrix*normal);
    vertex = uModelMatrix * position;
    v = uViewMatrix * vertex;
    gl_Position = uProjectionMatrix * v;
}