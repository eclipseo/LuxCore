#include <string>
namespace slg { namespace ocl {
std::string KernelSource_texture_bump_funcs = 
"#line 2 \"texture_bump_funcs.cl\"\n"
"\n"
"/***************************************************************************\n"
" * Copyright 1998-2015 by authors (see AUTHORS.txt)                        *\n"
" *                                                                         *\n"
" *   This file is part of LuxRender.                                       *\n"
" *                                                                         *\n"
" * Licensed under the Apache License, Version 2.0 (the \"License\");         *\n"
" * you may not use this file except in compliance with the License.        *\n"
" * You may obtain a copy of the License at                                 *\n"
" *                                                                         *\n"
" *     http://www.apache.org/licenses/LICENSE-2.0                          *\n"
" *                                                                         *\n"
" * Unless required by applicable law or agreed to in writing, software     *\n"
" * distributed under the License is distributed on an \"AS IS\" BASIS,       *\n"
" * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.*\n"
" * See the License for the specific language governing permissions and     *\n"
" * limitations under the License.                                          *\n"
" ***************************************************************************/\n"
"\n"
"//------------------------------------------------------------------------------\n"
"// Texture bump/normal mapping\n"
"//------------------------------------------------------------------------------\n"
"\n"
"#if defined(PARAM_HAS_BUMPMAPS)\n"
"\n"
"void Texture_Bump(\n"
"		const uint texIndex,\n"
"		__global HitPoint *hitPoint,\n"
"		const float sampleDistance\n"
"		TEXTURES_PARAM_DECL) {\n"
"	const float3 dpdu = VLOAD3F(&hitPoint->dpdu.x);\n"
"	const float3 dpdv = VLOAD3F(&hitPoint->dpdv.x);\n"
"	const float3 dndu = VLOAD3F(&hitPoint->dndu.x);\n"
"	const float3 dndv = VLOAD3F(&hitPoint->dndv.x);\n"
"\n"
"	// Calculate bump map value at intersection point\n"
"	const float base = Texture_GetFloatValue(texIndex, hitPoint\n"
"			TEXTURES_PARAM);\n"
"\n"
"	// Compute offset positions and evaluate displacement texIndex\n"
"	const float3 origP = VLOAD3F(&hitPoint->p.x);\n"
"	const float3 origShadeN = VLOAD3F(&hitPoint->shadeN.x);\n"
"	const float2 origUV = VLOAD2F(&hitPoint->uv.u);\n"
"\n"
"	float2 duv;\n"
"\n"
"	// Shift hitPointTmp.du in the u direction and calculate value\n"
"	const float uu = sampleDistance / length(dpdu);\n"
"	VSTORE3F(origP + uu * dpdu, &hitPoint->p.x);\n"
"	hitPoint->uv.u += uu;\n"
"	VSTORE3F(normalize(origShadeN + uu * dndu), &hitPoint->shadeN.x);\n"
"	const float duValue = Texture_GetFloatValue(texIndex, hitPoint\n"
"			TEXTURES_PARAM);\n"
"	duv.s0 = (duValue - base) / uu;\n"
"\n"
"	// Shift hitPointTmp.dv in the v direction and calculate value\n"
"	const float vv = sampleDistance / length(dpdv);\n"
"	VSTORE3F(origP + vv * dpdv, &hitPoint->p.x);\n"
"	hitPoint->uv.u = origUV.s0;\n"
"	hitPoint->uv.v += vv;\n"
"	VSTORE3F(normalize(origShadeN + vv * dndv), &hitPoint->shadeN.x);\n"
"	const float dvValue = Texture_GetFloatValue(texIndex, hitPoint\n"
"			TEXTURES_PARAM);\n"
"	duv.s1 = (dvValue - base) / vv;\n"
"\n"
"	// Restore HitPoint\n"
"	VSTORE3F(origP, &hitPoint->p.x);\n"
"	VSTORE2F(origUV, &hitPoint->uv.u);\n"
"\n"
"	// Compute the new dpdu and dpdv\n"
"	const float3 bumpDpdu = dpdu + duv.s0 * origShadeN;\n"
"	const float3 bumpDpdv = dpdv + duv.s1 * origShadeN;\n"
"	float3 newShadeN = normalize(cross(bumpDpdu, bumpDpdv));\n"
"\n"
"	// The above transform keeps the normal in the original normal\n"
"	// hemisphere. If they are opposed, it means UVN was indirect and\n"
"	// the normal needs to be reversed\n"
"	newShadeN *= (dot(origShadeN, newShadeN) < 0.f) ? -1.f : 1.f;\n"
"\n"
"	// Update HitPoint structure\n"
"	VSTORE3F(newShadeN, &hitPoint->shadeN.x);\n"
"	VSTORE3F(bumpDpdu, &hitPoint->dpdu.x);\n"
"	VSTORE3F(bumpDpdu, &hitPoint->dpdv.x);\n"
"}\n"
"\n"
"#if defined(PARAM_ENABLE_TEX_NORMALMAP)\n"
"void NormalMapTexture_Bump(\n"
"		const uint texIndex,\n"
"		__global HitPoint *hitPoint,\n"
"		const float sampleDistance\n"
"		TEXTURES_PARAM_DECL) {\n"
"	// Normal from normal map\n"
"	const __global Texture *texture = &texs[texIndex];\n"
"	float3 rgb = Texture_GetSpectrumValue(texture->normalMap.texIndex, hitPoint\n"
"			TEXTURES_PARAM);\n"
"	rgb = clamp(rgb, -1.f, 1.f);\n"
"\n"
"	// Normal from normal map\n"
"	float3 n = 2.f * rgb - (float3)(1.f, 1.f, 1.f);\n"
"\n"
"	const float3 oldShadeN = VLOAD3F(&hitPoint->shadeN.x);\n"
"	float3 dpdu = VLOAD3F(&hitPoint->dpdu.x);\n"
"	float3 dpdv = VLOAD3F(&hitPoint->dpdv.x);\n"
"	\n"
"	Frame frame;\n"
"	Frame_Set_Private(&frame, dpdu, dpdv, oldShadeN);\n"
"\n"
"	// Transform n from tangent to object space\n"
"	float3 shadeN = normalize(Frame_ToWorld_Private(&frame, n));\n"
"	shadeN *= (dot(oldShadeN, shadeN) < 0.f) ? -1.f : 1.f;\n"
"\n"
"	// Update dpdu and dpdv so they are still orthogonal to shadeN \n"
"	dpdu = cross(shadeN, cross(dpdu, shadeN));\n"
"	dpdv = cross(shadeN, cross(dpdv, shadeN));\n"
"\n"
"	// Update HitPoint structure\n"
"	VSTORE3F(shadeN, &hitPoint->shadeN.x);\n"
"	VSTORE3F(dpdu, &hitPoint->dpdu.x);\n"
"	VSTORE3F(dpdv, &hitPoint->dpdv.x);\n"
"}\n"
"#endif\n"
"\n"
"#endif\n"
; } }
